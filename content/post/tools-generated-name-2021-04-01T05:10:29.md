---
title: "Heroku with docker"
date: 2021-04-01T05:10:29
Description: ""
Tags: []
Categories: []
DisableComments: false
---
#### Install the Heroku CLI

Download and install the  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```bash
$ heroku login
```
#### Log in to Container Registry

You must have Docker set up locally to continue. You should see output when you run this command.
```bash
$ docker ps
```
Now you can sign into Container Registry.
```bash
$ heroku container:login
```
#### Push your Docker-based app

Build the Dockerfile in the current directory and push the Docker image.
```bash
$ heroku container:push web
```
#### Deploy the changes

Release the newly pushed images to deploy your app.
```bash
$ heroku container:release web
```
Reference:
[Deploying with Docker | Heroku Dev Center](https://devcenter.heroku.com/categories/deploying-with-docker)
[Container Registry & Runtime (Docker Deploys) | Heroku Dev Center](https://devcenter.heroku.com/articles/container-registry-and-runtime)

