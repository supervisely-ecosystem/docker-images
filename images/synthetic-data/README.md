# List of synthetic data applications:

- [flying-objects](https://github.com/supervisely-ecosystem/flying-objects)
- [synthetic-retail-products](https://github.com/supervisely-ecosystem/synthetic-retail-products)
- [synthetic-videos-for-tracking](https://github.com/supervisely-ecosystem/synthetic-videos-for-tracking)
- [stable-diffusion-app](https://github.com/supervisely-ecosystem/stable-diffusion-app)

## Custom docker images:

**supervisely/stable-diffusion-app:1.0.0**

- [stable-diffusion-app](https://github.com/supervisely-ecosystem/stable-diffusion-app)

## Dependencies per application:

```text
# base
supervisely==6.72.70
black
isort

# flying-objects
supervisely==6.72.70
albumentations==1.1.0
opencv-python==4.5.5.62

# synthetic-retail-products
supervisely==6.72.70
supervisely[augs]==6.72.70
opencv-python==4.5.5.62
albumentations==1.1.0

# synthetic-videos-for-tracking
supervisely==6.72.70

# stable-diffusion-app
supervisely==6.72.70
``````