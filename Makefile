run:
	PYTHONPATH=backend poetry run uvicorn backend.main:app --port $${PORT:-8300} --host 0.0.0.0

deploy-frontend:
	rsync -av --progress --stats frontend/dist pine:/srv/todo/frontend/
