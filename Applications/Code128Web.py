import gradio as gr
import code128


def code128_gen(text):
    text_list = text.split("\n")
    image_array = []
    for line in text_list:
        image_array.append((code128.image(line), line))
    return image_array


demo = gr.Interface(
    fn=code128_gen,
    inputs=[gr.Text(max_lines=20,
                    placeholder="P-7-A123B456",
                    autoscroll=True,
                    lines=20)],
    outputs=[gr.Gallery(format="jpeg",
                        object_fit="fill",
                        show_share_button=False,
                        show_download_button=False,
                        interactive=True)],
)

demo.launch(share=True)
