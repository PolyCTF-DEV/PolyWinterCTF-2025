FROM ubuntu:22.04

WORKDIR /app
COPY . /app
ENV CONFIG_PATH=/app/debug/config.json
RUN chmod +x /app/main
CMD /app/main
