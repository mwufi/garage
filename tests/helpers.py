import pickle

import gym

from tests.quirks import KNOWN_GYM_RENDER_NOT_IMPLEMENTED


def step_env(env, n=10, render=True):
    env.reset()
    for _ in range(n):
        _, _, done, _ = env.step(env.action_space.sample())
        if render:
            env.render()
        if done:
            break
    env.close()


def step_env_with_gym_quirks(test_case,
                             env,
                             spec,
                             n=10,
                             render=True,
                             serialize_env=False):
    if serialize_env:
        # Roundtrip serialization
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip.env.spec == env.env.spec
        env = round_trip

    env.reset()
    for _ in range(n):
        _, _, done, _ = env.step(env.action_space.sample())
        if render:
            if not spec.id in KNOWN_GYM_RENDER_NOT_IMPLEMENTED:
                env.render()
            else:
                with test_case.assertRaises(NotImplementedError):
                    env.render()
        if done:
            break

    if serialize_env:
        # Roundtrip serialization
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip.env.spec == env.env.spec

    env.close()


class AutoStopEnv(gym.Wrapper):
    """A env wrapper that stops rollout at step 100."""

    def __init__(self, env=None, env_name=""):
        if env_name:
            super().__init__(gym.make(env_name))
        else:
            super().__init__(env)
        self._rollout_step = 0
        self._max_path_length = 100

    def step(self, actions):
        self._rollout_step += 1
        next_obs, reward, done, info = self.env.step(actions)
        if self._rollout_step == self._max_path_length:
            done = True
            self._rollout_step = 0
        return next_obs, reward, done, info

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)
