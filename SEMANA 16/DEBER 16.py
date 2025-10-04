import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.task_listbox.get(index)
            if not task.startswith("[✓] "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "[✓] " + task)
                self.task_listbox.itemconfig(index, {'fg': 'gray'})
        else:
            messagebox.showinfo("Información", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("Información", "Seleccione una tarea para eliminar.")

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()