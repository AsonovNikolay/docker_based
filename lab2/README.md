minikube enable  
minikube addons enable ingress  

kubectl apply -f web_app/deployment.yaml  
kubectl apply -f web_app/service.yaml  
