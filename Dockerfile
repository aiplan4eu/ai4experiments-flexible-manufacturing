# Stage 1 - BUILD
FROM node:20 AS build
WORKDIR fm-frontend
COPY frontend .

ENV NG_CLI_ANALYTICS=ci
RUN npm install
RUN npm run build --prod

# Stage 2 - DEPLOY

FROM nginx:latest as ngi
COPY --from=build /fm-frontend/dist/gui /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR fm-backend
COPY backend .

# we install poetry
RUN apt-get update  \
    && apt-get install -y python3 pipx

RUN echo "export PATH=/root/.local/bin:${PATH}" >> /root/.bashrc

RUN pipx install poetry

RUN /root/.local/bin/poetry install

EXPOSE 8061
EXPOSE 8062
EXPOSE 12345

CMD ["./start.sh"]
