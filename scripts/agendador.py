import pandas as pd
import json
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate a subject schedule based on session dates."
    )
    parser.add_argument(
        "--subjects", required=True, help="Path to the JSON file containing subjects."
    )
    parser.add_argument(
        "--dates",
        required=True,
        help="Path to the CSV file containing session dates and their cancellation status.",
    )
    parser.add_argument(
        "--output", required=True, help="Path to the output CSV file for the schedule."
    )
    parser.add_argument(
        "--json_output",
        required=True,
        help="Path to the output JSON file for the detailed schedule.",
    )

    args = parser.parse_args()

    # Load inputs
    subjects = load_subjects(args.subjects)
    semester_dates = load_dates(args.dates)

    # Assign dates to subjects
    schedule = assign_subject_dates(subjects, semester_dates)

    # Save schedule to CSV
    schedule_df = pd.DataFrame(schedule).drop(columns=["dates"])
    schedule_df.to_csv(args.output, index=False)
    print(f"Schedule saved to {args.output}")

    # Save detailed schedule to JSON
    with open(args.json_output, "w", encoding="utf8") as json_file:
        json.dump(schedule, json_file, indent=2, ensure_ascii=False)
    print(f"Detailed schedule saved to {args.json_output}")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path.cwd().parent))

    import model as md

    main()
else:
    import model as md


def load_subjects(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def load_dates(file_path):
    # Load dates from a CSV file with a "date" column and an optional "canceled" column
    df = pd.read_csv(
        file_path, parse_dates=["date"], date_format="mixed", dayfirst=True
    )
    valid_dates = df.loc[df["canceled"] != True, "date"]
    return valid_dates


def assign_meet_dates(meets: list[md.Meet], dates: pd.Series) -> list[md.Meet]:
    schedule = []
    start_index = 0
    num_dates = dates.shape[0]

    for meet in meets:
        try:
            start_date = dates.iloc[start_index]
        except IndexError:
            break

        end_index = start_index + meet.date_span - 1

        if end_index >= num_dates:
            end_index = num_dates - 1

        _ = dates.iloc[end_index]
        date_range = dates.iloc[start_index : end_index + 1]

        meet.start_date = start_date.date()
        meet.dates = list(map(lambda t: t.date(), date_range.to_list()))
        schedule.append(meet)

        start_index = end_index + 1

    return schedule


def assign_subject_dates(
    subjects, semester_dates, sessions_column="sessions", name_column="name"
):
    schedule = []
    current_session_index = 0

    for subject in subjects:
        start_date = semester_dates.iloc[current_session_index]
        end_index = current_session_index + subject[sessions_column] - 1

        if end_index >= len(semester_dates):
            raise ValueError(
                "Not enough dates to schedule all subjects. Check your inputs."
            )

        end_date = semester_dates.iloc[end_index]
        subject_dates = semester_dates.iloc[
            current_session_index : end_index + 1
        ].tolist()

        schedule.append(
            {
                name_column: subject[name_column],
                sessions_column: subject[sessions_column],
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "dates": [date.strftime("%Y-%m-%d") for date in subject_dates],
            }
        )

        current_session_index = end_index + 1

    return schedule
