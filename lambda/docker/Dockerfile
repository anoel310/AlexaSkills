FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (update 'app.handler' as needed)
CMD ["lambda_function.lambda_handler"]