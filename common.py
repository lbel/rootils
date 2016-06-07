import sys
import ROOT

files = [ROOT.TFile.Open(arg) for arg in sys.argv[1:]]

def perform_trees(fn):
    for f in files:
        for key in f.GetListOfKeys():
            if key.GetClassName() != "TTree":
                continue
        tree_name = key.GetName()
        tree = f.Get(tree_name)
        if tree and isinstance(tree, ROOT.TTree):
            print("{}/{}".format(f.GetName(), tree_name))
            fn(tree)

