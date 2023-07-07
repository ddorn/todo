PYTHONPATH=backend 

run:
	poetry run uvicorn backend.main:app --port $${PORT:-8300} --host 0.0.0.0
