- I created a main.py file that returns the message in a format that is expected

- Run the simple application to make sure that it works

- I created a Dockerfile that installs the proper dependencies and runs the application

- Built the Dockerfile and run a container locally to make sure that it works:

  1. docker build -t rkostov/app-image:2.13 .
  2. docker run -d --name app-image rkostov/app-image
  3. docker exec -it app-image sh
  
- Running the <container-ip>:5000 gave back the same result as running localhost:5000 in the second step

- Used k3s for spinning up a local Kubernetes cluster

- Created a Helm chart using "helm create helm-chart"

- In the values.yaml file, changed the following things:

  1. Since I have the image locally, no need for it to fail searching for it online: 
     1. repository: rkostov/app-image
     2. pullPolicy: Never
  2. As per the request of having 4 replicas:
     1. replicaCount: 4
  3. As per the request of having service type LoadBalancer:
     1. type: LoadBalancer
  
- App version in the Chart.yaml file is set as following:

  1. appVersion: "2.13"

  This way I could use the Helm chart version to manipulate the deployment version and the following deployments

- The upgrades I would do in my current scenario with:

  1. helm upgrade helm-chart helm-chart/
  
  Having previously set a different appVersion.

- Deployments also would be as rolling updates anyway as a Kubernetes feature. It would not bring the previous ones
  down without having the newer ones up and ready.