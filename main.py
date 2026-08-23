import customtkinter as ctk
import requests
import threading

# Modern and dark appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NetworkTool(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Protocol Tester (Phase 1: HTTP)")
        self.geometry("850x600")

        # UI Elements
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter URL (e.g., example.com)", width=600)
        self.url_entry.pack(pady=20, padx=20)

        self.send_btn = ctk.CTkButton(self, text="Send GET Request", command=self.start_request)
        self.send_btn.pack(pady=10)

        self.response_box = ctk.CTkTextbox(self, width=800, height=400)
        self.response_box.pack(pady=20, padx=20)

    def start_request(self):
        # Disable the button to prevent spamming!
        self.send_btn.configure(state="disabled")
        self.response_box.delete("1.0", ctk.END)
        self.response_box.insert(ctk.END, "Sending request and waiting for response...\n")

        # Get the URL
        url = self.url_entry.get().strip()
        if not url:
            self.update_response("Input is empty! Please enter a valid URL.")
            return

        # Run the request in a separate daemon thread to avoid freezing the GUI
        threading.Thread(target=self.make_request, args=(url,), daemon=True).start()

    def make_request(self, url):
        # Auto-prepend https:// if missing
        if not url.startswith("http"):
            url = "https://" + url

        try:
            # Send GET request with a 10-second timeout
            response = requests.get(url, timeout=10)
            result = f"Status Code: {response.status_code}\n"
            result += "="*40 + "\nHeaders:\n"
            for k, v in response.headers.items():
                result += f"{k}: {v}\n"
            result += "="*40 + "\nBody:\n\n"
            result += response.text
        except Exception as e:
            result = f"Something went wrong (Error):\n{e}"

        # Safely update the GUI from the main thread
        self.after(0, self.update_response, result)

    def update_response(self, text):
        self.response_box.delete("1.0", ctk.END)
        self.response_box.insert(ctk.END, text)
        # Re-enable the button
        self.send_btn.configure(state="normal")

if __name__ == "__main__":
    app = NetworkTool()
    app.mainloop()
