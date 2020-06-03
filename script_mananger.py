import numpy as np
import pandas as pd
import torch

def script_manager(args, feature_method):

    audio=args[1]
    file_features=args[2]
    if args[3]=="false" or args[3]=="False":
        static=False
    elif args[3]=="true" or args[3]=="True":
        static=True
    else:
        raise ValueError(args[3] +" is not a valid argument for <static>. It should be only True or False")

    if args[4]=="false" or args[4]=="False":
        plots=False
    elif args[4]=="true" or args[4]=="True":
        plots=True
    else:
        raise ValueError(args[4] +" is not a valid argument for <plots>. It should be only True or False")

    if args[5]=="npy" or args[5]=="csv" or args[5]=="txt" or args[5]=="torch" or args[5]=="kaldi":
        fmt=args[5]
    else:
        raise ValueError(args[5]+ " is not a valid argument for <format>. It should be only csv, txt, npy, kaldi, or torch")

    if audio.find('.wav')!=-1 or audio.find('.WAV')!=-1:
        if fmt=="kaldi":
            feature_method.extract_features_file(audio, static=static, plots=plots, fmt=fmt, kaldi_file=file_features)
        else:
            features=feature_method.extract_features_file(audio, static=static, plots=plots, fmt=fmt)
            if fmt=="npy":
                np.save(file_features, np.hstack(features))
            elif fmt=="txt":
                np.savetxt(file_features, np.hstack(features))
            elif fmt=="csv":
                features.to_csv(file_features)
            elif fmt=="torch":
                torch.save(features, file_features)
            else:
                raise ValueError("Not valid output format")
    else:
        if fmt=="kaldi":
            feature_method.extract_features_path(audio, static=static, plots=plots, fmt=fmt, kaldi_file=file_features)
        else:
            features=feature_method.extract_features_path(audio, static=static, plots=plots, fmt=fmt)
            if fmt=="npy":
                np.save(file_features, features)
            elif fmt=="txt":
                np.savetxt(file_features, features)
            elif fmt=="csv":
                features.to_csv(file_features)
            elif fmt=="torch":
                torch.save(features, file_features)
            else:
                raise ValueError("Not valid output format")