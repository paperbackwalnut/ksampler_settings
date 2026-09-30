import comfy.samplers


class KSamplerSettings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                    },
                ),
                "steps": (
                    "INT",
                    {
                        "default": 20,
                        "min": 1,
                        "max": 10000,
                    },
                ),
                "cfg": (
                    "FLOAT",
                    {
                        "default": 8.0,
                        "min": 0.0,
                        "max": 100.0,
                        "step": 0.1,
                    },
                ),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "denoise": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                    },
                ),
            }
        }

    RETURN_TYPES = (
        "INT",
        "INT",
        "FLOAT",
        comfy.samplers.KSampler.SAMPLERS,
        comfy.samplers.KSampler.SCHEDULERS,
        "FLOAT",
    )

    RETURN_NAMES = (
        "seed",
        "steps",
        "cfg",
        "sampler_name",
        "scheduler",
        "denoise",
    )

    FUNCTION = "get_settings"
    CATEGORY = "utils/sampling"

    def get_settings(
        self,
        seed,
        steps,
        cfg,
        sampler_name,
        scheduler,
        denoise,
    ):
        return (
            seed,
            steps,
            cfg,
            sampler_name,
            scheduler,
            denoise,
        )


NODE_CLASS_MAPPINGS = {
    "KSamplerSettings": KSamplerSettings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KSamplerSettings": "KSampler Settings",
}