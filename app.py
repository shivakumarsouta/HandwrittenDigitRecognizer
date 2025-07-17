import gradio as gr
import tensorflow as tf

model = tf.keras.models.load_model('model.h5')

def recognize_digit(image):
    if image is not None:
        image = image.reshape(1, 28, 28, 1).astype('float32') / 255

        prediction = model.predict(image)
        return {str(i): float(prediction[0][i]) for i in range(10)}
    else:
        return ''
    
interface = gr.Interface(
    fn = recognize_digit,
    inputs = gr.Image(
        shape = (28, 28), 
        image_mode = 'L', 
        invert_colors = True, 
        source = 'canvas',
        label = 'Draw here'
        ),
    outputs = gr.Label(
        num_top_classes = 10,
        label = 'Prediction'
        ),
    live = True,
    title="Handwritten Digit Recognition",
    description="Draw a digit (0-9) and the model will predict what it is.",
    theme="soft",
)

interface.launch()