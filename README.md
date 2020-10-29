# Bookstore

- This is full stack project
	- The backend is python django restframework + grpcframework.
	- The frontend is react redux.

- To download it, clone : https://github.com/ccapeng/bookstore_grpc.git

- To start backend,
	- Make sure `python` and `pip` installed.
	- Then cd to `bookstore_grpc` directory.
	- For the first time, create virtual environment  
		`python -m venv env`
	- Then start the virtual environment `.\env\Scripts\activate`
	- Also for the very first time, run `pip install -r requirements.txt`
	- To start server, run `python manage.py grpcrunserver --dev 0.0.0.0:8003 `

	- [Django gRPC framework](https://djangogrpcframework.readthedocs.io/en/latest/index.html) has document of how to create proto buffer.
	
- Envoy Proxy :
	- Must have it in order to forward the frontend data to backend.
	- Copy `envoy\envoy-bookstore-grpc.yaml` to the linux environment. Since my computer is windows 10, I have wsl2 (Ubuntu20.04).
	- Please install `envoy` to wsl2.
	- Run `envoy -c envoy-bookstore-grpc.yaml`.  
		It's just easy to run it instead of bringing up docker.
	
	
- For the frontend,
	It's react redux, please find it at [https://github.com/ccapeng/bookstore-redux-grpc](https://github.com/ccapeng/bookstore-redux-grpc)  
	
	
- Known issues :

	- Book list, book id, title, category id , publisher id, author id.  
		Still looking how to output book id, title, category name, publisher name, author last name, author first name.  
		
	- In the book creation page, the none exist object exception raise if category, publisher, author id is 0. Can't create.  
		`book.service.py` is file should work on.
		From [django gRPC framework](https://djangogrpcframework.readthedocs.io/en/latest/index.html), I don't get much clue how to get it work on :
		- How to join table?
		- How to validate data? 
		Just leave it like that for now. If you find any document of how to do, please let me know.

	- It's my first draft to get gRPC react CRDU to work. Took a lot of efforts. I will see if I can get the known issues fix. Also, I am looking to use `go` as backend.
