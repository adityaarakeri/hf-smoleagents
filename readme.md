# HuggingFace SmoleAgent play ground

# pre reqs
- pipenv
- python >= 3.12

# install
```bash
pipenv install --python 3.12
```

### Langfuse keys

# Get keys for your project from the project settings page: https://cloud.langfuse.com
```py
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..." 
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..." 
# os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com" # 🇪🇺 EU region
os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```