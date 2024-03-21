require 'tk'
require 'tkextlib/tkimg'


root = TkRoot.new { title "Complex Loading Screen" }
root.geometry("600x400") 


image_path = "C:\Users\School\Desktop\School\loading.rb" 
image = TkPhotoImage.new(file: image_path)
label_with_image = TkLabel.new(root) { image image }.pack('side' => 'top', 'fill' => 'both', 'expand' => 'yes')


progress_frame = TkFrame.new(root).pack('side' => 'bottom', 'fill' => 'x')
progress_bar = TkLabel.new(progress_frame, bg: 'green', width: 0, anchor: 'w')
progress_bar.pack('side' => 'left', 'fill' => 'y')


Tk.update


total_steps = 100
total_steps.times do |step|
  sleep(0.05)
  progress_bar.configure('width' => (600 * (step + 1) / total_steps).to_i) s
  Tk.update
end


Tk.after(1000) { root.destroy } 

Tk.mainloop
