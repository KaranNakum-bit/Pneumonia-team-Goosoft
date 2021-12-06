import streamlit as st
from PIL import Image 
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image 


st.write("""# X-Ray Classification [Pneumonia/Normal]""")


temp = st.file_uploader("Upload X-Ray Image")

buffer = temp
temp_file = NamedTemporaryFile(delete=False)
if buffer:
    temp_file.write(buffer.getvalue())
    st.write(image.load_img(temp_file.name))


elif buffer is None:
  st.text("Oops! that doesn't look like an image. Try again.")

else:

 

  pavan_img = image.load_img(temp_file.name, target_size=(500, 500),color_mode='grayscale')

  #prediction messages
  pavan_preds =1
  #cnn.predict(pp_pavan_img)
  if pavan_preds>= 0.5:
    out = ('I am {:.2%} percent confirmed that this is a Pneumonia case'.format(pavan_preds[0][0]))
  
  else: 
    out = ('I am {:.2%} percent confirmed that this is a Normal case'.format(1-pavan_preds[0][0]))

  st.success(out)
  
  image = Image.open(temp)
  st.image(image,use_column_width=True)