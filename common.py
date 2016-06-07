import sys
import ROOT

files = [ROOT.TFile.Open(arg) for arg in sys.argv[1:]]

def perform_trees(fn):
    for f in files:
        __perform_trees_on_file(fn, f)

def __perform_trees_on_file(fn, f):
    for key in f.GetListOfKeys():
        if key.GetClassName() == "TDirectoryFile":
            __perform_trees_on_file(fn, f.Get(key.GetName()))
        elif key.GetClassName() == "TTree":
            tree_name = key.GetName()
            tree = f.Get(tree_name)
            if tree and isinstance(tree, ROOT.TTree):
                print("{}/{}".format(f.GetName(), tree_name))
                fn(tree)
        else:
            print("Not a TTree {}".format(key.GetName()))
            continue
