minikube enable  
minikube addons enable ingress  

kubectl apply -f web_app/deployment.yaml  
kubectl apply -f web_app/service.yaml  
kubectl port-forward service/product-service 8080:80  


Deployment используем для управления подами
Service используем для сетевых настроек приложения 
(3 пода по приколу сделаны, смысловой нагрузки нет)  

Это без звездочки  

Файлы можно конечно объеденить и запускать одной командой, но в целом не критично
