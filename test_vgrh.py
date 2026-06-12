from vgrh import calculate_vgrh

source = {
    "title": "MELD: A Multimodal Dataset",
    "url": "https://aclanthology.org/P19-1050/"
}

score = calculate_vgrh(
    source,
    "Compare MELD and IEMOCAP"
)

print(score)