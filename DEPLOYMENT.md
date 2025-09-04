# Deployment Instructions

## Prerequisites

1. Install Docker and Docker Compose on your server.
2. Clone your repository to the server.
   ```bash
   git clone https://github.com/mmemew07-bot/-ai-cloud-storage.git
   cd -ai-cloud-storage
   ```
3. Set up the `.env` file with your production values.

## Build and Deploy

```bash
# Make the deploy script executable
chmod +x deploy.sh

# Run the deployment
./deploy.sh
```

## Verify Deployment

- Frontend: http://your-server-ip
- Backend API: http://your-server-ip/api/health
- API Documentation: http://your-server-ip/api/docs

## Scaling

```bash
# Scale backend services if needed
docker-compose up -d --scale backend=3
```

## Monitoring

- Check logs:
  ```bash
docker-compose logs -f
  ```
- Monitor resources:
  ```bash
docker stats
  ```

## Updates

1. Pull latest changes:
    ```bash
    git pull
    ```
2. Run deployment script again:
    ```bash
    ./deploy.sh
    ```