# Custom processing block example (Python)

This is an example of a custom processing block, which you can load in the Edge Impulse studio. See the docs: [Building custom processing blocks](https://docs.edgeimpulse.com/docs/custom-blocks).

Additionally, this repo demonstrates how to use Octave inside Edge Impulse Studio.  The key steps are

1. Install octave into the container (apt install octave liboctave-dev)

2. Install Octave package dependencies.  Installing via the Dockerfile will save time and avoid having to wait for an install each time you train.
- Note, on Linux or inside containers, if a pacakge added to setup.m fails to build, you can also try to install it via apt install, example: apt install octave-control

See [the following line in the Dockerfile](Dockerfile#L25)
```
RUN octave setup.m
```

3. Invoke Octave from Python via the Oct2Py package
- Start your octave instance, and run your octave script file so your functions will be added to the Octave namespace.
Do this outside of the generate_features function, so that your Octave instance will persist across samples
```
oc = oct2py.Oct2Py()

```
- Invoke functions like so: result = oc.my_func([1,2,3])
- Numpy arrays are also valid input