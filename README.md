# Python Lambda Logistics
The Python Lambda Logistics (`pll`) library is designed to assist with an automated deployment for `Python 3` AWS Lambda functions.

As you will no doubt discover, as soon as you require more than the basic libraries, you need to start creating what 
are known as 'deployment packages' (zip files with all dependencies) for pushing even basic scripts up to AWS.

These packages require that the libraries are compiled for amazon's version of linux (which is executing the code on 
your behalf).

Not helpful if, like me, your development machine isn't running AWS Linux...

Some of the main libraries this has helped me so far with packaging:

* SQLAlchemy
* Pandas
* NumPy


## Underlying Process
`pll` aims to simplify the above by automating the build of your `requirements.txt` file in a `Docker` image of 
`awslinux`.

1. Create working directories in your current project
    * `Build`  --  contains compiled `site-packages` for future re-use
    * `Dist`  --  outputted lambda `zip` for upload to AWS
2. Check for a local docker image of `saracen9/python-lambda` or pull down
3. Mount the following locations into the docker image
    * `Build` --> /tmp/app/psite-packages
    * `Dist` --> /tmp/app/zipped-package
    * YourAppplicationRoot --> /app
4. Run the container and compile
5. Shutdown and £profit
6. (Opt) push code to AWS (Coming soon)

The original Dockerfile used to create the image is contained within the package source code for those who want to hack 
their own.

## Usage
To manually run and configure the docker container use the below command. 
```bash
docker run --rm --name py-lamb-compiler \
    -v ~/my/app:/app \
    -v ~/my/app/dist:/tmp/app/dist \
    -v ~/my/app/build:/tmp/app/build \
    saracen9/python-lambda
```

Alternatively install the library and put a `pll.yaml` in the root of your application.

```yaml
packaging:
  app_root: '/my/app'
  build_path: '/my/app/build'
  dist_path: '/my/app/dist'
```

You can then run `python -m pll` and package the application from any script. As an additional option pass in the 
`--config` switch to define your own config file.

In addition, relative paths to the `cwd` are accepted. These are then converted to absolute paths at runtime E.g.

```yaml
packaging:
  app_root: ''  # current directory
  build_path: 'build/'  # current directory/build
  dist_path: 'dist/'  # current directory/dist
```