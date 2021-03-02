# Todo

This repository contains a small website that I use to track my todos. 
Obviously, I spend more time building it that it will ever save me, but this is an other story.

The repo is split into two parts, one for the frontend and one for the backend.

### The backend

The backend is build with FastAPI in python which is an incredible too to build APIs... fast !
I also use `sqlalchemy` to handle the sqlite database and `alembic` for the migrations.

To run the backend, you need those three libraries (provided by the `flake.nix`) along with uvicorn.
Then `start` will run the server on `$PORT` which is 
by default 8300. With `start dev` you should see the
server at [localhost:8300/docs](http://localhost:8300/docs).


### The frontend

The frontend is build with [VueJs](https://vuejs.com)... and also a ton of libraries since my node_modules is more than 200M large!
The styling is made with [tailwindcss](https://tailwindcss.com) which is quite efficient and keeps everthing together.

The website can be build with `npm run build` and for development purposes served with `npm run serve`.
When the backend is running locally, the modifications
on the sources can be witnessed in real-time. 

If you build the frontend, there is no need to use `serve` as it will be served by the backend automatically.