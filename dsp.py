import numpy as np
import oct2py

# Add the functions in our script to Octave's namespace
oc = oct2py.Oct2Py()


def generate_features(implementation_version, draw_graphs, raw_data, axes, sampling_freq, scale_axes):
    # features is a 1D array, reshape so we have a matrix
    raw_data = raw_data.reshape(int(len(raw_data) / len(axes)), len(axes))

    features = []
    graphs = []

    # split out the data from all axes
    for ax in range(0, len(axes)):
        fx = raw_data[:, ax]

        # potentially scale data from sensor
        fx = np.array(fx, dtype='f') * scale_axes

        fx = oc.rms_test(fx)

        # we need to return a 1D array again, so flatten here again
        features.append(fx)

    return {
        'features': features,
        'graphs': graphs,
        # if you use FFTs then set the used FFTs here (this helps with memory optimization on MCUs)
        'fft_used': [],
        'output_config': {
            # type can be 'flat', 'image' or 'spectrogram'
            'type': 'flat',
            'shape': {
                # shape should be { width, height, channels } for image, { width, height } for spectrogram
                'width': len(features)
            }
        }
    }
