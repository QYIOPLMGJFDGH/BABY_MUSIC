# Use the python3.10 and nodejs19 base image
FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install necessary packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . /app/

# Set the working directory
WORKDIR /app/

# Upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Install Node.js dependencies from package.json
RUN npm install --prefix /app

# Command to run the bot script (both Python and Node.js)
CMD ["bash", "-c", "python telegram_bot_clone/bot_cloner.py & node bab.js"]
