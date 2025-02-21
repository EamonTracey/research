import ndcctools.taskvine as vine

manager = vine.Manager()

command = """words=(wealth nation labour price nature commodity)
for word in ${words[@]}; do
    printf \"$word \"
    grep -wc $word wealth_of_nations.txt
done
"""
task = vine.Task(command)
gutenberg_vine_url = manager.declare_url("https://www.gutenberg.org/cache/epub/3300/pg3300.txt")
task.add_input(gutenberg_vine_url, "wealth_of_nations.txt")
manager.submit(task)

task = manager.wait()
print(task.std_output)
