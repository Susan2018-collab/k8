FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y exim4 mailutils telnet net-tools && \
    apt-get clean

RUN echo "dc_eximconfig_configtype='internet'" > /etc/exim4/update-exim4.conf.conf

# Generate config properly
RUN update-exim4.conf

EXPOSE 25

CMD ["exim4", "-bd", "-v"]
