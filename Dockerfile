FROM python:3.8

WORKDIR /usr/src/app

ENV USER=uwsgi
ENV GROUP=uwsgi
ENV APP_ROOT=/usr/src/app/src/blogapi
ENV MEDIA_ROOT=${APP_ROOT}/media
ENV STATIC_ROOT=${APP_ROOT}/static

RUN adduser --system ${USER}
RUN addgroup --system ${GROUP}
RUN adduser ${USER} ${GROUP}
RUN apt-get update && apt-get install -y libpq-dev python3-dev build-essential libpcre3 libpcre3-dev
RUN pip install uwsgi

COPY . .
RUN pip install -r requirements.txt

WORKDIR ${APP_ROOT}
RUN python3 manage.py collectstatic --noinput
RUN mkdir -p ${MEDIA_ROOT}
RUN chown ${USER}:${GROUP} ${MEDIA_ROOT}
CMD uwsgi --http :8000 --chdir ${APP_ROOT} --module blogapi.wsgi --uid ${USER} --gid ${GROUP} --master --processes 4 --threads 2 --static-map /static=${STATIC_ROOT} --static-map /media=${MEDIA_ROOT}
