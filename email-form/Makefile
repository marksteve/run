.PHONY: dev build deploy
dev: venv/bin/pip-sync requirements.txt
	venv/bin/pip-sync
requirements.txt: venv/bin/pip-compile requirements.in
	venv/bin/pip-compile \
	--no-index \
	--no-emit-trusted-host \
	requirements.in > requirements.txt
venv/bin/pip-compile venv/bin/pip-sync: venv
	venv/bin/pip install wheel pip-tools
venv:
	python3 -m venv venv
build:
	gcloud builds submit --tag gcr.io/$(PROJECT_ID)/email-form
deploy:
	gcloud beta run deploy \
		--region us-central1 \
		--image gcr.io/$(PROJECT_ID)/email-form \
		--set-env-vars=MG_DOMAIN=$(MG_DOMAIN) \
		--set-env-vars=MG_API_KEY=$(MG_API_KEY) \
		--set-env-vars=REDIRECT_URL=$(REDIRECT_URL) \
		--set-env-vars=EMAIL_FROM=$(EMAIL_FROM) \
		--set-env-vars=EMAIL_TO=$(EMAIL_TO) \
		--allow-unauthenticated \
		--platform managed

