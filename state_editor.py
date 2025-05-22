import os
import json

BOTS_DIR = "bots"

def list_bots():
    bots = [d for d in os.listdir(BOTS_DIR) if os.path.isdir(os.path.join(BOTS_DIR, d))]
    return bots

def load_state(bot_id):
    path = os.path.join(BOTS_DIR, bot_id, "jeangrey_state.json")
    with open(path, "r") as f:
        return json.load(f), path

def save_state(state, path, new_id=None):
    if new_id and new_id != state["bot_id"]:
        new_path = os.path.join(BOTS_DIR, new_id)
        os.rename(os.path.dirname(path), new_path)
        path = os.path.join(new_path, "jeangrey_state.json")
        state["bot_id"] = new_id
    with open(path, "w") as f:
        json.dump(state, f, indent=4)
    return path

def rename_bot(state, path):
    print(f"Current bot_id: {state['bot_id']}")
    new_id = input("New bot_id: ").strip()
    if new_id:
        save_state(state, path, new_id)
        print(f"[✓] Renamed to {new_id}")

def edit_tags(state, path):
    print(f"Current tags: {state['tags']}")
    action = input("Add or Remove a tag? (a/r): ").strip().lower()
    if action == "a":
        tag = input("New tag to add: ").strip()
        if tag and tag not in state["tags"]:
            state["tags"].append(tag)
    elif action == "r":
        tag = input("Tag to remove: ").strip()
        if tag in state["tags"]:
            state["tags"].remove(tag)
    save_state(state, path)
    print("[✓] Tags updated.")

def kill_bot(bot_id):
    confirm = input(f"Are you sure you want to delete {bot_id}? (yes/no): ").lower()
    if confirm == "yes":
        os.system(f"rm -rf {os.path.join(BOTS_DIR, bot_id)}")
        print(f"[💀] {bot_id} deleted.")

def manage_bot(bot_id):
    state, path = load_state(bot_id)
    while True:
        print(f"\n=== Managing: {bot_id} ===")
        print(f"1) View State\n2) Rename Bot\n3) Edit Tags\n4) Kill Bot\n0) Back")
        choice = input("Choice: ").strip()
        if choice == "1":
            print(json.dumps(state, indent=4))
        elif choice == "2":
            rename_bot(state, path)
        elif choice == "3":
            edit_tags(state, path)
        elif choice == "4":
            kill_bot(bot_id)
            break
        elif choice == "0":
            break

def main():
    while True:
        bots = list_bots()
        print("\n=== Team EVA - Mesh Bot State Editor ===")
        if not bots:
            print("No bots found.")
            break
        for i, b in enumerate(bots):
            print(f"{i+1}) {b}")
        print("0) Exit")
        try:
            choice = int(input("Select a bot to manage: "))
            if choice == 0:
                break
            if 1 <= choice <= len(bots):
                manage_bot(bots[choice-1])
        except ValueError:
            continue

if __name__ == "__main__":
    main()
