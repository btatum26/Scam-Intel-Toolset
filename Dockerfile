FROM python:3.11-slim

WORKDIR /app

# Copy the tracker script and template
COPY tracker.py .
COPY index.html .

# Create a volume point for logs
RUN mkdir -p /app/private
VOLUME /app/private

# Expose the port
EXPOSE 8080

# Run the tracker
CMD ["python", "tracker.py"]
