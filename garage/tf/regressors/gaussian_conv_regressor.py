"""Gaussian Conv Regressor."""
import tensorflow as tf

from garage.core import Serializable
from garage.tf.core import LayersPowered
from garage.tf.core import Parameterized


class GaussianConvRegressor(LayersPowered, Serializable, Parameterized):
    """A regressor fits a Gaussian distribution to the outputs using a cnn."""

    def __init__(self,
                 input_shape,
                 output_dim,
                 conv_filter_dims,
                 conv_num_filters,
                 conv_strides,
                 conv_padding="VALID",
                 name="GaussianConvRegressor",
                 mean_network=None,
                 hidden_sizes=(32, 32),
                 hidden_nonlinearity=tf.nn.tanh,
                 optimizer=None,
                 optimizer_args=None,
                 use_trust_region=True,
                 step_size=0.01,
                 learn_std=True,
                 init_std=1.0,
                 adaptive_std=False,
                 std_share_network=False,
                 std_hidden_sizes=(32, 32),
                 std_nonlinearity=None,
                 normalize_inputs=True,
                 normalize_outputs=True,
                 subsample_factor=1.0):
        """Add doc."""
        pass
