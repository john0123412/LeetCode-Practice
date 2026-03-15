# AI Coding Agent Instructions for This Workspace

## Project Overview

This is a **learning & practice codebase** containing multiple independent algorithm and data structure solutions. The workspace is organized as a collection of programming exercises spanning multiple programming languages and domains:

- **Algorithm Problems**: LeetCode-style problems (array manipulation, median finding, etc.)
- **Web Applications**: React components (Simplex Solver visualization)
- **Scripting**: Python utilities for learning purposes
- **Tools & Config**: VS Code extensions and Continue.dev AI agent configuration

## Key Architecture Patterns

### Multi-Language Project Structure
- **Python files** (`.py`): Algorithm solutions with type hints (`List`, `float` type annotations)
- **JavaScript/React** (`.js`): Interactive UI components (e.g., Simplex Solver with state management)
- **Configuration files**: `.vscode/settings.json`, `.continue/agents/new-config.yaml`

### Testing & Development
- **Python testing**: Uses `unittest` framework (configured in `.vscode/settings.json`)
- **Test discovery pattern**: Files matching `*test.py` are automatically discovered
- **No build step**: Direct file execution (Python scripts run directly, React via dev tools)

## Code Patterns & Conventions

### Python Conventions
1. **Type Annotations**: Always use type hints with `typing.List`, `float` returns
   ```python
   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
   ```

2. **Algorithm Structure**: Solution classes with method-based implementations
   ```python
   class Solution:
       def methodName(self, param: Type) -> ReturnType:
           # Implementation
   ```

3. **Test Entry Point**: `if __name__ == "__main__":` pattern for test cases

### JavaScript/React Conventions
1. **Component Structure**: Functional components with React hooks (`useState`)
2. **State Management**: Local component state for UI logic
3. **Icon Library**: Uses `lucide-react` for UI icons
4. **Algorithm Implementation**: Complex algorithms (Simplex solver) implemented in JavaScript

## Essential Workflows

### Running Tests
```bash
python -m unittest discover -v -s . -p "*test.py"
```
Configure via `.vscode/settings.json` under Python testing settings.

### Development Tools
- **VS Code Extensions**: Check `.vscode/extensions.json` for recommended extensions
- **Continue.dev Integration**: AI agent configuration in `.continue/agents/new-config.yaml` supports multiple models:
  - OpenAI GPT-5
  - Ollama (Qwen2.5-coder-7b)
  - Anthropic Claude-4-Sonnet

### File Organization
- Root-level files are independent exercises (no shared dependencies)
- Each solution is self-contained with its own `if __name__ == "__main__":` block

## Integration Points & Dependencies

### External Libraries
- **React & Lucide Icons**: For UI components in JavaScript/React files
- **Typing Module**: Python's built-in for type hints
- **No external frameworks**: Most Python solutions are standard library only

### Cross-Language Notes
- No inter-language dependencies detected
- Each file/component is independently executable
- AI agents should treat each file as a separate context unless explicitly importing from other files

## Development Principles

1. **Self-Contained Solutions**: Each algorithm/component should work independently
2. **Type Safety First**: Python code emphasizes type hints; React uses prop-based typing
3. **Readable Over Clever**: Code prioritizes clarity for learning purposes
4. **Example-Driven Testing**: Solutions include `print()` statements showing expected outputs

## Useful Files for Understanding Project Context

- [.vscode/settings.json](.vscode/settings.json) - Python testing configuration
- [.continue/agents/new-config.yaml](.continue/agents/new-config.yaml) - AI model configuration
- [1](..) - Simplex Solver React component (complex algorithm visualization)
- [2](..) - Binary search median algorithm (advanced Python)
- [demo](..) - Simple array manipulation solution
- [demo1](..) - Python kwargs example
