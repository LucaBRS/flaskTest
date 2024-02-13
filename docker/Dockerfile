FROM python:3.9

# working directory
WORKDIR /app

# Copy  requirements
COPY requirements.txt /app

# Copy the entire application code to the container
COPY app.py /app

# Copy the gas.json file into the image
COPY gas.json /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the default command to run when the container starts
CMD ["python", "app.py"]