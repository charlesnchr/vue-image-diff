# vue-image-diff
vue component for multiple image comparison.

Web-App: [https://github.com/whwnsdlr1/image-diff](https://github.com/whwnsdlr1/image-diff)
jsfiddle: 
## Build
build project as below
```
git clone https://github.com/whwnsdlr1/vue-image-diff
cd vue-image-diff
yarn run build
```

## Usage
1. load images by drag & drop or dialog that you can open by panel click.
2. (optional) if the images are different sizes, the other images will be resized to the first image size.
you can set order of images using file name(index key and value, seperated by two underscore).
ex) barbara__index__0.jpg, cameraman__index__1.jpg, salesman__index__3.png...
3. diff !
```
mouse & touch drag - panning
mouse wheel & pinch to zoom - zoom in / out
mouse doubleclick - select reference image
```

- x: coordinate x.
- y: coordinate y.
- scale: scale, scale is applied before coordinate.(panning)
- diff: turn on / off diff mode.
- ref: reference image to diff. you can change ref by frame click in diff mode.
- tolerance: if difference value(Mean Square Error) is greater than or equal tolerance, pixel is set difference-tag. opposite, set same-tag less than tolerance. ![equation](http://latex.codecogs.com/png.latex?%5Csum_%7BP%7D%5E%7Bp%7D%28%5Csqrt%7B%28R_%7Bp1%7D-R_%7Bp2%7D%29%5E%7B2%7D%20&plus;%20%28G_%7Bp1%7D-G_%7Bp2%7D%29%5E%7B2%7D%20&plus;%20%28B_%7Bp1%7D-B_%7Bp2%7D%29%5E%7B2%7D%7D%29)
- home: move to image load page.
- rearrange: rearrange frames. drag and drop.
- setting
```
- define image size: image size to be resized. only can set before load images.
- show overlay text: show / hidden file name and description.
- frame row count: frames row count.
- border width: border width. limit to [0, 40)
- border color: border color.
```

## Browser support - (tested)
- Google Chrome 77+
- Google Chrome 77+ on Android 9+
- Mozilla FireFox 68+

## Project setup
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Third-party libraries
### Dependencies
- vue: [https://github.com/vuejs/vue](https://github.com/vuejs/vue)
- cornerstone-core: [https://github.com/cornerstonejs/cornerstone](https://github.com/cornerstonejs/cornerstone)
- jpeg-js: [https://github.com/eugeneware/jpeg-js](https://github.com/eugeneware/jpeg-js)
- pngjs: [https://github.com/arian/pngjs](https://github.com/arian/pngjs)
- element-resize-event: [https://github.com/KyleAMathews/element-resize-event](https://github.com/KyleAMathews/element-resize-event)
- vue-lodash: [https://github.com/Ewocker/vue-lodash](https://github.com/Ewocker/vue-lodash)
- vue-toasted: [https://github.com/shakee93/vue-toasted](https://github.com/shakee93/vue-toasted)

### Dev-Dependencies
- @vue/cli-plugin-babel
- @vue/cli-plugin-eslint
- @vue/cli-service
- babel-eslint
- eslint
- eslint-plugin-vue
- vue-template-compiler

## TO-DO
- support other image format(bmp, tiff)
