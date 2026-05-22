# Quelora — quelora-detoxify
# Copyright (C) 2026 Germán Zelaya — https://quelora.org
# SPDX-License-Identifier: AGPL-3.0-only
#
# This file is part of Quelora. See the LICENSE file for terms.

"""
@module ML/Detoxify
@description FastAPI wrapper for the Detoxify multilingual moderation model.
Provides a local REST interface to evaluate text toxicity.
@version 1.0.0
"""

from fastapi import FastAPI
from pydantic import BaseModel
from detoxify import Detoxify

app = FastAPI(title="Quelora ML - Detoxify API")

# Load the multilingual model eagerly at startup.
# The cache volume prevents re-downloading the weights on every container restart.
model = Detoxify('multilingual')

class Comment(BaseModel):
    text: str

@app.post("/moderate")
def moderate_comment(comment: Comment):
    """
    Evaluates the given text for toxicity.
    Executed in a threadpool (synchronous def) to prevent CPU-bound predictions
    from blocking the main ASGI event loop.
    """
    results = model.predict(comment.text)
    
    # Convert numpy float32 results to standard Python floats for JSON serialization
    return {category: float(score) for category, score in results.items()}
