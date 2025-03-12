render:
	quarto render --cache-refresh

clean:
	rm -r ./public/*

preview:
	quarto preview

serve:
	npx http-server ./public