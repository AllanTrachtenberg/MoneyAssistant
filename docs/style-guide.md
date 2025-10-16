# MoneyAssistant Style Guide

This document outlines the coding standards, naming conventions, and best practices for the MoneyAssistant project.

## Table of Contents

- [Git and Branching Conventions](#git-and-branching-conventions)
  - [Branch Naming Conventions](#branch-naming-conventions)
    - [Branch Type Prefixes](#branch-type-prefixes)
    - [Examples](#examples)
    - [Best Practices](#best-practices)
  - [Commit Message Conventions](#commit-message-conventions)
    - [Commit Types](#commit-types)
    - [Examples](#examples-1)
  - [Pull Request Guidelines](#pull-request-guidelines)
  - [Merge Strategy](#merge-strategy)
    - [Feature Branches → Dev Branch](#feature-branches--dev-branch)
    - [Dev Branch → Main Branch](#dev-branch--main-branch)
    - [Merge Process](#merge-process)
- [Code Style](#code-style)
  - [General Principles](#general-principles)
  - [Naming Conventions](#naming-conventions)
    - [Variables and Functions](#variables-and-functions)
    - [Constants](#constants)
    - [Classes and Components](#classes-and-components)
    - [CSS Classes](#css-classes)
- [File Organization](#file-organization)
  - [Directory Structure](#directory-structure)
  - [File Naming](#file-naming)
- [Documentation Standards](#documentation-standards)
  - [Code Comments](#code-comments)
  - [README and Documentation](#readme-and-documentation)
  - [Issue and PR Templates](#issue-and-pr-templates)
    - [Available Issue Templates](#available-issue-templates)
    - [Template Configuration](#template-configuration)
    - [Story vs Task Guidelines](#story-vs-task-guidelines)
    - [How to Use Issue Templates](#how-to-use-issue-templates)
    - [Writing Quality Issues](#writing-quality-issues)
    - [Issue Labels and Organization](#issue-labels-and-organization)
    - [Template Benefits](#template-benefits)
    - [PR Template Usage](#pr-template-usage)
- [Enforcement](#enforcement)

## Git and Branching Conventions

### Branch Naming Conventions

When creating branches to address GitHub issues, follow this consistent naming pattern:

```
<type>/<issue-number>-<short-description>
```

#### Branch Type Prefixes

- **`feature/`** - New features or functionality
- **`fix/`** - Bug fixes
- **`refactor/`** - Code refactoring without changing functionality
- **`docs/`** - Documentation updates
- **`test/`** - Adding or updating tests
- **`chore/`** - Maintenance tasks (dependencies, build config, etc.)
- **`config/`** - Configuration changes

#### Examples

```bash
# Features
feature/12-expense-categories
feature/15-user-authentication
feature/8-budget-tracking

# Bug fixes
bugfix/9-fix-date-validation
fix/23-resolve-calculation-error
hotfix/5-security-vulnerability

# Documentation
docs/3-create-style-guide
docs/16-api-documentation
```

#### Best Practices

1. **Use kebab-case** for descriptions (lowercase with hyphens)
2. **Keep descriptions short** but descriptive (2-4 words)
3. **Include issue numbers** to link branches to GitHub issues
4. **Avoid special characters** (stick to letters, numbers, and hyphens)

### Commit Message Conventions

Follow the conventional commit format:

```
<type>(<scope>): <description>

[optional body]
```

#### Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools

#### Examples

```bash
feat(auth): add user login functionality

fix(calculator): resolve incorrect total calculation
Fixes #23

docs(readme): update installation instructions
```

### Pull Request Guidelines

1. **Use clear, descriptive PR titles** that explain what the PR accomplishes from a user/business perspective
2. **Reference the issue** in the PR description using closing keywords
3. **Include a summary** of changes made in the description
4. **Use the PR template** (automatically loaded when creating PRs)
5. **Complete the checklist** before requesting review
6. **Ensure tests pass** before requesting review
7. **Self-review your code** before submitting the PR

#### PR Title Guidelines

**Use conventional commit format for PR titles** - follow the same pattern as commit messages:

```
<type>(<scope>): <description>
```

```
✅ Good PR Titles:
feat(expenses): add expense categories functionality
fix(auth): resolve login validation errors
perf(dashboard): improve loading performance
docs(readme): update installation instructions
refactor(api): restructure expense endpoints

❌ Avoid in PR titles:
feat(expenses): add categories (#12)       # Don't include issue numbers
Add expense categories functionality       # Missing type and scope
Updates and fixes                          # Too vague
Fix stuff                                  # Not descriptive
```

**Note:** Issue numbers belong in the PR description (`Closes #12`), not in the title. This avoids confusion with the automatic PR number that GitHub assigns.

#### PR Template

All pull requests automatically use the template (`.github/pull_request_template.md`) which includes:

```markdown
## Description
Brief description of what this PR accomplishes.

## Changes Made
- List specific changes made
- Each change should be clear and concise

## Related Issue
Closes #

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have tested my changes
- [ ] I have updated documentation if needed
```

#### Linking PRs to Issues

**Use closing keywords in the "Related Issue" section:**
- `Closes #12` - Automatically closes issue when PR merges
- `Fixes #23` - Same as closes, good for bug fixes
- `Resolves #45` - Same as closes, good for feature requests

### Merge Strategy

#### Feature Branches → Dev Branch
- **Use "Squash and merge"** when merging feature branches into the `dev` branch
- This keeps the commit history clean by combining all commits from the feature branch into a single commit
- The squashed commit message should be descriptive and reference the issue number
- After merging, delete the feature branch to keep the repository clean

#### Dev Branch → Main Branch
- **Use "Create a merge commit"** when merging `dev` into `main`
- This preserves the development history and creates a clear release record
- Tag the merge commit with a version number (e.g., `v1.0.0`, `v1.1.0`)
- Only merge to `main` when `dev` contains a complete, tested feature set ready for release
- Write descriptive merge commit messages that summarize the release

#### Merge Process

**For Feature Development:**
1. Create feature branch from `dev`: `git switch -c feature/12-expense-categories`
2. Work on the feature with multiple commits
3. Create pull request targeting `dev` branch
4. Review and approve the pull request
5. Use "Squash and merge" to merge into `dev`
6. Delete the feature branch after successful merge

**For Releases:**
1. Ensure `dev` branch contains all features for the release
2. Run full test suite on `dev` branch
3. Create pull request from `dev` to `main`
4. Review the complete changeset
5. Use "Create a merge commit" to merge into `main`
6. Tag the release: `git tag -a v1.0.0 -m "Release version 1.0.0"`
7. Keep `dev` branch for continued development

## Code Style

### General Principles

1. **Consistency** - Follow established patterns within the codebase
2. **Documentation** - Comment complex logic and business rules

### Naming Conventions

#### Variables and Functions
- Use **snake_case** for variables and functions
- Use descriptive names that explain purpose
- Avoid abbreviations unless they're widely understood

```python
# Good
user_expenses = []
def calculate_monthly_total():
    pass

# Avoid
usr_exp = []
def calc_mth_tot():
    pass
```

#### Constants
- Use **SCREAMING_SNAKE_CASE** for constants
- Group related constants in dictionaries or enums

```python
# Good
API_ENDPOINTS = {
    'EXPENSES': '/api/expenses',
    'CATEGORIES': '/api/categories'
}

MAX_EXPENSE_AMOUNT = 10000
```

#### Classes and Components
- Use **PascalCase** for classes
- Use descriptive names that indicate the class's purpose

```python
# Good
class ExpenseCalculator:
    pass

class ExpenseForm:
    pass

class DashboardHeader:
    pass
```

## File Organization

### File Naming

- Use **snake_case** for file names
- Include the file type or purpose in the name when helpful
- Group related files in directories

```python
# Good
expense_form.py
user_service.py
api_constants.py
dashboard_page.py

# Avoid
ExpenseForm.py
userservice.py
constants.py
```

## Documentation Standards

### Code Comments

1. **Explain why, not what** - Focus on business logic and decisions
2. **Keep comments up to date** - Remove or update outdated comments
3. **Use docstrings** for function documentation

```python
def calculate_period_total(expenses, start_date, end_date):
    """
    Calculates the total expenses for a given time period
    
    Args:
        expenses (list): List of expense objects
        start_date (datetime): Start of the period
        end_date (datetime): End of the period
    
    Returns:
        float: Total amount of expenses
    """
    # Filter expenses within the date range
    # Business rule: Include expenses on start date, exclude end date
    filtered_expenses = [
        expense for expense in expenses 
        if start_date <= expense.date < end_date
    ]
    
    return sum(expense.amount for expense in filtered_expenses)
```

### Issue and PR Templates

Use consistent templates for issues and pull requests to maintain quality and completeness of information.

#### Available Issue Templates

We provide structured templates for different types of issues in the `.github/ISSUE_TEMPLATE/` directory:

**Story Template** (`story.md`) - Use for describing features from the user's perspective:
- Follows the standard "As a... I want... So that..." format
- Includes acceptance criteria with Given/When/Then scenarios
- Tagged with `story` label

**Task Template** (`task.md`) - Use for technical implementation work:
- Describes specific technical work to be completed
- Links to parent user stories
- Tagged with `task` label

**Bug Report Template** (`bug_report.md`) - Use when reporting problems or errors:
- Structured format for reproducible bug reports
- Tagged with `bug` label

#### Template Configuration

The `.github/ISSUE_TEMPLATE/config.yml` file configures the issue creation experience:
- **Enforces template usage** by disabling blank issues
- **Provides alternative contact methods** for different types of requests
- **Guides users** to appropriate channels (Discussions, email for security)

#### Story vs Task Guidelines

**Use Story Template when:**
- Describing functionality from user's perspective
- Defining user value
- Planning what features to build


**Use Task Template when:**
- Breaking down stories into implementable work
- Defining technical implementation details
- Assigning specific development work
- Tracking progress on technical components

**Relationship Example:**
```
Story #15: Add expense categorization functionality
├── Task #16: Create Category database model and API endpoints
├── Task #17: Add category dropdown to expense form UI
├── Task #18: Create category management page (CRUD operations)
└── Task #19: Add spending by category chart component
```

#### How to Use Issue Templates

1. **Navigate to Issues** in the GitHub repository
2. **Click "New Issue"** to see template selection menu
3. **Choose appropriate template** based on your need:
   - **Story** - For user-focused features
   - **Task** - For technical implementation
   - **Bug Report** - For problems or errors
4. **Fill out all sections** - Don't delete template structure
5. **Add relevant labels** if not automatically applied
6. **Link related issues** using `#issue-number` syntax

#### Template Benefits

- **Consistent information** - Ensures all necessary details are provided
- **Faster resolution** - Structured information helps respond quickly
- **Better organization** - Automatic labeling helps categorize issues
- **Professional appearance** - Shows the project follows best practices
- **Clear workflow** - Separates user requirements from technical implementation

#### PR Template Usage

All pull requests automatically use the template (`.github/pull_request_template.md`) which includes:
- **Description** - Brief overview of changes
- **Changes Made** - Specific list of modifications
- **Related Issue** - Link using closing keywords (`Closes #12`)
- **Checklist** - Quality control before review

---

## Enforcement

This style guide should be enforced through:

1. **Code reviews** - All code changes should be reviewed for adherence
2. **Team discussions** - Regular reviews and updates to the style guide

---

*This style guide is a living document and should be updated as the project evolves*