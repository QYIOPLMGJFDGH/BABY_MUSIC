FROM nikolaik/python-nodejs:python3.10-nodejs19

# Update package list and install required packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy your application code into the container
COPY . /app/

# Install required Python packages
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Make the shell script executable
RUN chmod +x start_and_clone.sh

# Command to run your shell script
CMD ["./start_and_clone.sh"]
