# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Alok Kumar <ialokkumarsing0@gmail.com>" \
      org.label-schema.name="my-site-varnish" \
      org.label-schema.description="my-site Varnish image." \
      org.label-schema.vendor="Alok Kumar"

COPY etc/varnish.vcl /etc/varnish/default.vcl
