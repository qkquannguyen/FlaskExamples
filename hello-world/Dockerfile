# ----------------------------------------------------------------------------------------------- #
# This is a simple Flask Web Application that is deployed to your localhost using docker. The app #
# simply shows a message to the world that it is a healthy running application on the web!        #
#                                                                                                 #
# This is the Dockerfile for the application that will install needed dependencies for this app.  #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #

# --------------------------------------- Pull Base Image --------------------------------------- #
FROM centos:7.3.1611


# ------------------------------------- Run Command as Root ------------------------------------- #
USER root


# ---------------------------------------- Build Command ---------------------------------------- #
RUN yum -y update && yum clean all
RUN yum -y install epel-release && yum clean all
RUN yum -y install python34 && yum clean all
RUN yum -y install python34-libs python34-setuptools python34-pip gcc python34-devel git && yum clean all
RUN easy_install-3.4 pip && yum clean all
RUN pip install --upgrade pip


# ---------------------------- Initialize Web Applications Directory ---------------------------- #
RUN mkdir /HelloWorld_App
WORKDIR /HelloWorld_App
ADD . .


# ------------------------------------- Install Requirement ------------------------------------- #
RUN pip3 install -r requirements.txt


# --------------------------------------- Expose any Port --------------------------------------- #
EXPOSE 8080


# ----------------------------------- Define Default Commands ----------------------------------- #
CMD ["python3", "helloworld_manage.py", "runserver"]
