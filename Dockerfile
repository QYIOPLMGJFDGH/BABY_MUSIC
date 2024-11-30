# Use Node.js base image
FROM node:18

# Set the working directory
WORKDIR /usr/src/app

# Copy Node.js package files (for installing dependencies)
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Install Python and other dependencies
RUN apt-get update \
    && apt-get install -y python3 python3-pip ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Command to run both Node.js bot and Python script
CMD ["bash", "-c", "node bot.js & python SONALI/main.py"]
