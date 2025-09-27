import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista para almacenar las tareas (texto y estado de completado)
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())  # Añadir con Enter

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.mark_completed)
        self.complete_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar las tareas
        self.listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", lambda event: self.mark_completed())  # Doble clic para completar

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append((task, False))  # False = no completada
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task, completed = self.tasks[index]
            self.tasks[index] = (task, not completed)  # Cambiar estado
            self.update_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            display_text = f"[✔] {task}" if completed else task
            self.listbox.insert(tk.END, display_text)
            if completed:
                self.listbox.itemconfig(tk.END, {'fg': 'gray'})  # Estilo para completadas

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
