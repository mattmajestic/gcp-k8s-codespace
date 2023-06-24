FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copy session tracking script to container
COPY session_tracking.py /usr/local/bin/session_tracking.py

# Install dependencies
RUN pip3 install jsonschema datetime

# Set up environment variables
ENV SESSION_DATA_FILE="/session/session_data.json"

# Set script permissions
RUN chmod +x /usr/local/bin/session_tracking.py

# Set the working directory
WORKDIR /workspace

# Start the session tracking script
CMD ["/usr/local/bin/session_tracking.py"]