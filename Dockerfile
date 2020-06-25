FROM ubuntu:18.04

# Install system dependencies
RUN apt-get update \
    && apt-get upgrade \ 
    && apt-get install -y python3 wget unzip default-jre make cmake libz-dev g++ git minisat python-pip

# Install sugar   
RUN wget http://bach.istc.kobe-u.ac.jp/sugar/package/sugar-v2-3-3.zip -P /tmp \
    && cd /tmp \
    && unzip sugar-v2-3-3.zip \
    && cd /tmp/sugar-v2-3-3/ \
    && mkdir -p /usr/local/lib/sugar/ \
    && mv /tmp/sugar-v2-3-3/bin/sugar-v2-3-3.jar /usr/local/lib/sugar/sugar-v2-3-3.jar \
    && mv /tmp/sugar-v2-3-3/bin/sugar /bin/

# Install glucose
RUN wget https://www.labri.fr/perso/lsimon/downloads/softwares/glucose-syrup-4.1.tgz -P /tmp \
    && cd /tmp \
    && tar -xzf /tmp/glucose-syrup-4.1.tgz  \
    && cd /tmp/glucose-syrup-4.1/simp \
    && make rs \
    && mv glucose* /bin/glucose

RUN cd /tmp && rm -rf * 

COPY . /app
WORKDIR /app

# Install python libraries
RUN pip install -r requirements.txt

ENTRYPOINT python main.pyc 
