FROM node:20-slim AS frontend-build
WORKDIR /build
COPY package.json ./
RUN npm install
COPY index.html vite.config.js tailwind.config.js postcss.config.js ./
COPY public/ ./public/
COPY src/ ./src/
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
COPY --from=frontend-build /build/dist ./dist
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
