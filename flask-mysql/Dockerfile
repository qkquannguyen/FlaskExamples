# ----------------------------------------------------------------------------------------------- #
# This is the Dockerfile for the application that will install needed dependencies for this app.  #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# --------------------------------------- Pull Base Image --------------------------------------- #
FROM centos:7.3.1611

# ------------------------------------- Run Command as Root ------------------------------------- #
USER root


# Update and Clean
RUN yum -y update && yum clean all


# ---------------------------------------- Build Command ---------------------------------------- #
RUN yum -y update && yum clean all
RUN yum -y install epel-release && yum clean all
RUN yum -y install python34 && yum clean all
RUN yum -y install python34-libs python34-setuptools mysql-connector-python && yum clean all
RUN yum -y install mysql-devel python34-pip gcc python34-devel git && yum clean all
RUN easy_install-3.4 pip && yum clean all
RUN pip install --upgrade pip


# ---------------------------- Initialize Web Applications Directory ---------------------------- #
RUN mkdir /Flask_MySQL_App
WORKDIR /Flask_MySQL_App
ADD . .


# ------------------------------------- Install Requirement ------------------------------------- #
RUN pip3 install -r requirements.txt


# --------------------------------------- Expose any Port --------------------------------------- #
EXPOSE 5000


# ----------------------------------- Define Default Commands ----------------------------------- #
CMD ["python3", "flask_mysql_manage.py", "runserver"]