This is a repo for lfx mentorship application

## How to run it

you can use `minikube` to create a cluster
- `minikube start`

set the docker environment to minikube
- `eval (minikube docker-env)`

build the application image
- `cd quiz2/src&&docker build -f docker/Dockerfile  -t lfx/buddy:latest ./python/`

create the deployment and service
- `kubectl apply -f ./k8s`

create a minikube tunnel so that we can access our cluster from outside
- `minikube tunnel`


visit `http://127.0.0.1/buddy/list`
expected output: pod ips list
['172.17.0.7', '172.17.0.8', '172.17.0.6']

To uninstall, run `kubectl delete -f ./k8s`
